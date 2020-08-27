"""
Tests exercising the admin aspects of the datastore module.

Copyright (C) 2020 Nicholas H.Tollervey (ntoll@ntoll.org).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
from unittest import mock
from django.test import TestCase
from django.core.exceptions import ValidationError
from datastore import admin
from datastore import models


class UserCreationFormTestCase(TestCase):
    """
    Exercizes the custom methods and validation of the UserCreationForm used in
    the site admin.
    """

    def test_init(self):
        """
        Ensure autofocus is set for the username field.
        """
        f = admin.UserCreationForm()
        self.assertTrue(
            f.fields[f._meta.model.USERNAME_FIELD].widget.attrs["autofocus"]
        )

    def test_clean_password2(self):
        """
        The form ensures the two password fields match.
        """
        f1 = admin.UserCreationForm(
            data={
                "username": "test_user",
                "email": "test@user.com",
                "password1": "xyzzy2001",
                "password2": "xyzzy2001",
            }
        )
        self.assertTrue(f1.is_valid())
        f2 = admin.UserCreationForm(
            data={
                "username": "test_user",
                "email": "test@user.com",
                "password1": "xyzzy2001",
                "password2": "2001xyzzy",
            }
        )
        self.assertFalse(f2.is_valid())
        self.assertEqual(
            f2.errors["password2"], ["The two password fields didn't match."]
        )

    def test_post_clean(self):
        """
        Further password validation (using Django's built-in password
        validator) happens immediately after the form is cleaned.
        """
        f = admin.UserCreationForm(
            data={
                "username": "test_user",
                "email": "test@user.com",
                "password1": "xyzzy2001",
                "password2": "xyzzy2001",
            }
        )
        pwv = mock.MagicMock()
        error = ValidationError("Boom")
        pwv.validate_password = mock.MagicMock(side_effect=error)
        f.add_error = mock.MagicMock()
        with mock.patch("datastore.admin.password_validation", pwv):
            f.is_valid()
        f.add_error.assert_called_once_with("password2", error)

    def test_save(self):
        """
        Ensure the password is set against the user during the saving process.
        """
        mock_user = mock.MagicMock()
        mock_save = mock.MagicMock()
        mock_save.return_value = mock_user
        with mock.patch("datastore.admin.forms.ModelForm.save", mock_save):
            f = admin.UserCreationForm(
                data={
                    "username": "test_user",
                    "email": "test@user.com",
                    "password1": "xyzzy2001",
                    "password2": "xyzzy2001",
                }
            )
            f.is_valid()
            result = f.save()
            self.assertEqual(result, mock_user)
            mock_user.set_password.assert_called_once_with(
                f.cleaned_data["password1"]
            )
            mock_user.save.assert_called_once_with()


class UserChangeFormTestCase(TestCase):
    """
    Exercizes the custom methods and validation of the UserChangeForm used in
    the site admin.
    """

    def test_init(self):
        """
        Password help text is updated.
        """
        u = models.User.objects.create_user(
            username="test_user", email="test@user.com", password="password"
        )
        f = admin.UserChangeForm(u)
        self.assertIsNotNone(f.fields.get("password").help_text)

    def test_clean_password(self):
        """
        Ensure the initial value of the password (not the one from the form
        field) is always used when cleaning.
        """
        u = models.User.objects.create_user(
            username="test_user", email="test@user.com", password="password"
        )
        f = admin.UserChangeForm(u)
        f.initial = mock.MagicMock()
        f.clean_password()
        f.initial.get.assert_called_once_with("password")
