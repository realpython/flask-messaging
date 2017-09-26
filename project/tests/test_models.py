# project/tests/test_models.py


from flask_testing import TestCase
from project import db
from project import create_app
from project.api.models import CommentCategory, CommentObject, Comments


class TestCommentModel(TestCase):
    """Tests for the Comment model."""

    def create_app(self):
        app = create_app(config_name='testing')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_comment_category(self):
        """Ensure comment_category model behaves correctly."""
        comment_category = CommentCategory('justatest')
        db.session.add(comment_category)
        db.session.commit()
        self.assertTrue(comment_category.id)
        self.assertEqual(comment_category.comment_category, 'justatest')
        self.assertTrue(comment_category.date_created)

    def test_create_comment_object(self):
        """Ensure comment_object model behaves correctly."""
        comment_object = CommentObject('Staff', 1)
        db.session.add(comment_object)
        db.session.commit()
        self.assertTrue(comment_object.id)
        self.assertEqual(comment_object.object_type, 'Staff')
        self.assertTrue(comment_object.date_created)

    def test_create_comment(self):
        """Ensure comment model behaves correctly."""
        comment = Comments(1, 1, 'justatest')
        db.session.add(comment)
        db.session.commit()
        self.assertTrue(comment.id)
        self.assertEqual(comment.comment, 'justatest')
        self.assertTrue(comment.date_created)
