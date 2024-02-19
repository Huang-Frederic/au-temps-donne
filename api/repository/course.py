from model.course import Course
from database.db import db
from app import app

class CourseRepo():        
    
    def select_one_by_id(self, course_id: int) -> Course:
        try:
            user = Course.query.filter_by(course_id=course_id).first()
            return user
        except Exception:
            raise #UserAccessDbException(user_id=user_id, method="getting")
        
    
    # select_one_by_title ?

    
    def select_all(self) -> list[Course]:
        try:
            courses = Course.query.all()
            if not courses:
                return None
            return courses
        except Exception:
            raise #UserAccessDbException(user_id=None, method="getting")


    def insert(self, new_course: Course) -> None:
        try:
            with app.app_context():
                db.session.add(new_course)
                db.session.commit()
                db.session.close()
        except Exception:
            raise #UserAccessDbException(user_id=None, method="creating")
    

    def update(self, course_id: int, update_course: Course) -> None:
        try:
            with app.app_context():
                course = Course.query.filter_by(course_id=course_id).first()
                course.title = update_course.title
                course.description = update_course.description
                db.session.commit()
                db.session.close()
        except Exception:
            raise #UserAccessDbException(user_id=user_id, method="updating")


    def delete(self, course_id: int) -> None:
        try:
            course = Course.query.filter_by(course_id=course_id).first()
            with app.app_context():
                db.session.delete(course)
                db.session.commit()
                db.session.close()
        except Exception:
            raise #UserAccessDbException(user_id=user_id, method="deleting")