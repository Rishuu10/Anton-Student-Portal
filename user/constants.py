import enum


class CustomEnum(enum.Enum):

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class UserTypes(CustomEnum):
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    ADMIN = "ADMIN"


USER_APP_MAPPING = {
    UserTypes.STUDENT.value: 'student',
    UserTypes.TEACHER.value: 'teacher',
    UserTypes.ADMIN.value : 'admin',
}

class GenderTypes(CustomEnum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    CANNOT_SPECIFY = "CANNOT_SPECIFY"


class Messages(CustomEnum):
    LOGIN_FAILURE = "Username and Password doesn't match"