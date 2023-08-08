from django.core.management.base import BaseCommand
from a1.models import *
from faker import Faker
import pytz
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING('Starting...'))
        fake = Faker()

        authors = self.__create_authors(fake)
        books = self.__create_books(fake, authors)
        self.__create_reviews(fake, books)
        self.__create_sales(books)

        self.stdout.write(self.style.SUCCESS(f'Successfully seed database'))

    def __create_authors(self, fake):
        authors = []
        for _ in range(50):
            name = fake.name()
            birthday = fake.date_of_birth(minimum_age=18, maximum_age=100)
            birthday = datetime.combine(birthday, datetime.min.time(), tzinfo=pytz.UTC)
            country = fake.country()
            description = fake.paragraph()

            author = Author(name=name, birthday=birthday, country=country, description=description)
            author.save()
            authors.append(author)

        self.stdout.write(self.style.WARNING(f'Authors seeded'))
        return authors        

    def __create_books(self, fake, authors):
        books = []
        for _ in range(300):
            author = random.choice(authors)
            book = Book(
                name=fake.catch_phrase(),
                summary=fake.paragraph(),
                date_of_publication=datetime.combine(
                fake.date_between(start_date='-30y', end_date='today'), datetime.min.time(), tzinfo=pytz.UTC),
                author=author
            )
            book.save()
            books.append(book)

        self.stdout.write(self.style.WARNING(f'Books seeded'))
        return books

    def __create_reviews(self, fake, books):
        for book in books:
            num_reviews = random.randint(1, 10)
            for _ in range(num_reviews):
                review = Review(
                    book=book,
                    score=random.randint(1, 5),
                    review=fake.paragraph(),
                    number_of_up_votes=random.randint(0,1000)
                )
                review.save()

        self.stdout.write(self.style.WARNING(f'Reviews seeded'))

    def __create_sales(self, books):
        for book in books:
            num_years_of_sales = random.randint(5, 10)
            for i in range(num_years_of_sales):
                sale_date = book.date_of_publication + timedelta(days=365*i)
                sale = Sale(
                    book=book,
                    year=sale_date.year,
                    sales=random.randint(100, 1000)
                )
                sale.save()
                
        self.stdout.write(self.style.WARNING(f'Sales seeded'))