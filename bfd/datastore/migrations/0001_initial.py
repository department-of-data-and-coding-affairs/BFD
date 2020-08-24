# Generated by Django 3.0.8 on 2020-08-20 16:17

import datastore.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Namespace",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="The namespace's name identifying who is tagging data to objects.",
                        max_length=64,
                        unique=True,
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="A short description for more context about the Namespace.",
                        max_length=512,
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The date and time this namespace was created.",
                    ),
                ),
                (
                    "updated_on",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time this namespace was last updated.",
                    ),
                ),
                (
                    "admins",
                    models.ManyToManyField(
                        help_text="Users who administer the namespace.",
                        related_name="admins",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        help_text="The user who created the namespace.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="namespace_created_by_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        help_text="The user who last updated the namespace.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="namespace_updated_by_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="The tag's name identifying what is being tagged to objects.",
                        max_length=64,
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="A short description for more context about the tag.",
                        max_length=512,
                    ),
                ),
                (
                    "type_of",
                    models.CharField(
                        choices=[
                            ("s", "string"),
                            ("b", "boolean"),
                            ("i", "integer"),
                            ("f", "float"),
                            ("d", "datetime"),
                            ("u", "duration"),
                            ("a", "binary"),
                            ("p", "pointer"),
                        ],
                        help_text="Defines the type of data this tag stores.",
                        max_length=1,
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        editable=False,
                        help_text="A UUID representing the namespace/tag path.",
                    ),
                ),
                (
                    "private",
                    models.BooleanField(
                        default=False,
                        help_text="If true, data associated with this tag is private.",
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The date and time this tag was created.",
                    ),
                ),
                (
                    "updated_on",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time this tag was last updated.",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        help_text="The user who created the tag.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="tag_created_by_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "namespace",
                    models.ForeignKey(
                        help_text="The namespace to which this tag belongs.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Namespace",
                    ),
                ),
                (
                    "readers",
                    models.ManyToManyField(
                        help_text="If the tag is private, users who can read data added via the tag.",
                        related_name="readers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        help_text="The user who last updated the tag.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="tag_updated_by_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        help_text="Users who can add data via the tag.",
                        related_name="users",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StringValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "object_id",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="The unique unicode identifier for the object.",
                        max_length=512,
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        editable=False,
                        help_text="A UUID representing the namespace/tag path.",
                    ),
                ),
                (
                    "last_updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time the value was last updated.",
                    ),
                ),
                (
                    "value",
                    models.TextField(
                        help_text="The string data annotated onto the object via the namespace/tag."
                    ),
                ),
                (
                    "last_updated_by",
                    models.ForeignKey(
                        help_text="The user who most recently updated the value.",
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "namespace",
                    models.ForeignKey(
                        help_text="The namespace used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Namespace",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        help_text="The tag used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Tag",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PointerValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "object_id",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="The unique unicode identifier for the object.",
                        max_length=512,
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        editable=False,
                        help_text="A UUID representing the namespace/tag path.",
                    ),
                ),
                (
                    "last_updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time the value was last updated.",
                    ),
                ),
                (
                    "value",
                    models.URLField(
                        help_text="The URL value annotated onto the object via the namespace/tag.",
                        max_length=512,
                    ),
                ),
                (
                    "last_updated_by",
                    models.ForeignKey(
                        help_text="The user who most recently updated the value.",
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "namespace",
                    models.ForeignKey(
                        help_text="The namespace used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Namespace",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        help_text="The tag used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Tag",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IntegerValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "object_id",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="The unique unicode identifier for the object.",
                        max_length=512,
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        editable=False,
                        help_text="A UUID representing the namespace/tag path.",
                    ),
                ),
                (
                    "last_updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time the value was last updated.",
                    ),
                ),
                (
                    "value",
                    models.IntegerField(
                        help_text="The integer data annotated onto the object via the namespace/tag."
                    ),
                ),
                (
                    "last_updated_by",
                    models.ForeignKey(
                        help_text="The user who most recently updated the value.",
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "namespace",
                    models.ForeignKey(
                        help_text="The namespace used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Namespace",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        help_text="The tag used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Tag",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FloatValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "object_id",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="The unique unicode identifier for the object.",
                        max_length=512,
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        editable=False,
                        help_text="A UUID representing the namespace/tag path.",
                    ),
                ),
                (
                    "last_updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time the value was last updated.",
                    ),
                ),
                (
                    "value",
                    models.FloatField(
                        help_text="The float data annotated onto the object via the namespace/tag."
                    ),
                ),
                (
                    "last_updated_by",
                    models.ForeignKey(
                        help_text="The user who most recently updated the value.",
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "namespace",
                    models.ForeignKey(
                        help_text="The namespace used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Namespace",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        help_text="The tag used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Tag",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DurationValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "object_id",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="The unique unicode identifier for the object.",
                        max_length=512,
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        editable=False,
                        help_text="A UUID representing the namespace/tag path.",
                    ),
                ),
                (
                    "last_updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time the value was last updated.",
                    ),
                ),
                (
                    "value",
                    models.DurationField(
                        help_text="The duration annotated onto the object via the namespace/tag."
                    ),
                ),
                (
                    "last_updated_by",
                    models.ForeignKey(
                        help_text="The user who most recently updated the value.",
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "namespace",
                    models.ForeignKey(
                        help_text="The namespace used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Namespace",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        help_text="The tag used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Tag",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DateTimeValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "object_id",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="The unique unicode identifier for the object.",
                        max_length=512,
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        editable=False,
                        help_text="A UUID representing the namespace/tag path.",
                    ),
                ),
                (
                    "last_updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time the value was last updated.",
                    ),
                ),
                (
                    "value",
                    models.DateTimeField(
                        help_text="The datetime annotated onto the object via the namespace/tag."
                    ),
                ),
                (
                    "last_updated_by",
                    models.ForeignKey(
                        help_text="The user who most recently updated the value.",
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "namespace",
                    models.ForeignKey(
                        help_text="The namespace used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Namespace",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        help_text="The tag used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Tag",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BooleanValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "object_id",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="The unique unicode identifier for the object.",
                        max_length=512,
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        editable=False,
                        help_text="A UUID representing the namespace/tag path.",
                    ),
                ),
                (
                    "last_updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time the value was last updated.",
                    ),
                ),
                (
                    "value",
                    models.BooleanField(
                        help_text="The boolean data annotated onto the object via the namespace/tag."
                    ),
                ),
                (
                    "last_updated_by",
                    models.ForeignKey(
                        help_text="The user who most recently updated the value.",
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "namespace",
                    models.ForeignKey(
                        help_text="The namespace used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Namespace",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        help_text="The tag used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Tag",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BinaryValue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "object_id",
                    models.SlugField(
                        allow_unicode=True,
                        help_text="The unique unicode identifier for the object.",
                        max_length=512,
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        editable=False,
                        help_text="A UUID representing the namespace/tag path.",
                    ),
                ),
                (
                    "last_updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time the value was last updated.",
                    ),
                ),
                (
                    "value",
                    models.FileField(
                        help_text="The binary value annotated onto the object via the namespace/tag.",
                        upload_to=datastore.models.upload_to,
                    ),
                ),
                (
                    "mime",
                    models.CharField(
                        help_text="The mime type defining the type of binary value stored.",
                        max_length=256,
                    ),
                ),
                (
                    "last_updated_by",
                    models.ForeignKey(
                        help_text="The user who most recently updated the value.",
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "namespace",
                    models.ForeignKey(
                        help_text="The namespace used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Namespace",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        help_text="The tag used to annotate data onto the object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datastore.Tag",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="tag",
            constraint=models.UniqueConstraint(
                fields=("namespace", "name"), name="unique-namespace-tag"
            ),
        ),
        migrations.AddConstraint(
            model_name="stringvalue",
            constraint=models.UniqueConstraint(
                fields=("object_id", "namespace", "tag"), name="unique-str-val"
            ),
        ),
        migrations.AddConstraint(
            model_name="pointervalue",
            constraint=models.UniqueConstraint(
                fields=("object_id", "namespace", "tag"),
                name="unique-pointer-val",
            ),
        ),
        migrations.AddConstraint(
            model_name="integervalue",
            constraint=models.UniqueConstraint(
                fields=("object_id", "namespace", "tag"), name="unique-int-val"
            ),
        ),
        migrations.AddConstraint(
            model_name="floatvalue",
            constraint=models.UniqueConstraint(
                fields=("object_id", "namespace", "tag"),
                name="unique-float-val",
            ),
        ),
        migrations.AddConstraint(
            model_name="durationvalue",
            constraint=models.UniqueConstraint(
                fields=("object_id", "namespace", "tag"),
                name="unique-duration-val",
            ),
        ),
        migrations.AddConstraint(
            model_name="datetimevalue",
            constraint=models.UniqueConstraint(
                fields=("object_id", "namespace", "tag"),
                name="unique-datetime-val",
            ),
        ),
        migrations.AddConstraint(
            model_name="booleanvalue",
            constraint=models.UniqueConstraint(
                fields=("object_id", "namespace", "tag"),
                name="unique-bool-val",
            ),
        ),
        migrations.AddConstraint(
            model_name="binaryvalue",
            constraint=models.UniqueConstraint(
                fields=("object_id", "namespace", "tag"),
                name="unique-binary-val",
            ),
        ),
    ]
