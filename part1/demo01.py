class Student(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        if not cls._instance:

            cls._instance == super().__new__(cls, *args, **kwargs)

        return cls._instance


st1 = Student()
st2 = Student()

print(st1 is st2)
