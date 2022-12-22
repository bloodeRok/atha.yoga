# Generated by Django 4.1.4 on 2022-12-21 19:58

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(max_length=512)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_%(app_label)s.%(class)s_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=64)),
                ("description", models.TextField(blank=True)),
                (
                    "course_type",
                    models.CharField(
                        choices=[("ONLINE", "Online"), ("VIDEO", "Video")],
                        max_length=30,
                    ),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("STARTING", "Starting"),
                            ("CONTINUER", "Continuer"),
                            ("ADVANCED", "Advanced"),
                        ],
                        max_length=30,
                    ),
                ),
                ("single", models.BooleanField(default=False)),
                ("duration", models.DurationField()),
                ("start_datetime", models.DateTimeField()),
                ("deadline_datetime", models.DateTimeField(null=True)),
                (
                    "complexity",
                    models.CharField(
                        choices=[
                            ("EASY", "Easy"),
                            ("MEDIUM", "Medium"),
                            ("HARD", "Hard"),
                        ],
                        max_length=30,
                    ),
                ),
                ("link", models.URLField()),
                ("link_info", models.CharField(blank=True, max_length=100)),
                ("repeat_editing", models.BooleanField(default=False)),
                (
                    "payment",
                    models.CharField(
                        choices=[
                            ("PAYMENT", "Payment"),
                            ("DONATION", "Donation"),
                            ("FREE", "Free"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "price",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=0)
                        ]
                    ),
                ),
                (
                    "favorites",
                    models.ManyToManyField(
                        blank=True,
                        related_name="favorite_courses",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Занятие",
                "verbose_name_plural": "Занятия",
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("text", models.TextField()),
                (
                    "star_rating",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=1),
                            django.core.validators.MaxValueValidator(limit_value=5),
                        ]
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_%(app_label)s.%(class)s_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
            },
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.IntegerField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="courses.course",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Билет",
                "verbose_name_plural": "Билеты",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("start_at", models.DateTimeField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lessons",
                        to="courses.course",
                    ),
                ),
                ("participants", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "уроки",
            },
        ),
        migrations.CreateModel(
            name="CourseReview",
            fields=[
                (
                    "review_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="courses.review",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="courses.course",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзыв о курсе",
                "verbose_name_plural": "Отзывы о курсе",
            },
            bases=("courses.review",),
        ),
        migrations.CreateModel(
            name="CourseComment",
            fields=[
                (
                    "comment_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="courses.comment",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="courses.course",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий к курсу",
                "verbose_name_plural": "Комментарии к курсу",
            },
            bases=("courses.comment",),
        ),
    ]
