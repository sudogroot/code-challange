import factory
import uuid
import random


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = "books.profile"
        strategy = factory.CREATE_STRATEGY

    user_name = factory.Sequence(lambda n: "userss {}".format(n))


class BookFactory(factory.DjangoModelFactory):
    class Meta:
        model = "books.book"
        strategy = factory.CREATE_STRATEGY

    title = factory.Sequence(lambda n: "book {} title".format(n))
    isbn = factory.LazyAttribute(lambda obj: str(uuid.uuid1()))
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def comments(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # the nbr of comments to create were passed in, use them
            for i in range(extracted):
                CommentsFactory(book=self)

    @factory.post_generation
    def stars(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # the nbr of comments to create were passed in, use them
            for i in range(extracted):
                StarsFactory(book=self)


class CommentsFactory(factory.DjangoModelFactory):
    class Meta:
        model = "books.comment"
        strategy = factory.CREATE_STRATEGY

    content = factory.Sequence(lambda n: "comment content {}".format(n))
    book = factory.SubFactory(BookFactory)
    user = factory.SubFactory(UserFactory)


class StarsFactory(factory.DjangoModelFactory):
    class Meta:
        model = "books.stars"
        strategy = factory.CREATE_STRATEGY

    stars = random.randint(1, 5)
    book = factory.SubFactory(BookFactory)
    user = factory.SubFactory(UserFactory)
