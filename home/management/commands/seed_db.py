from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from instructor.models import Instructor
from home.models import Image
from classes.models import Class
import datetime


class Command(BaseCommand):
    
    help = 'Seeds the database with initial data'


    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        superuser_username = 'Andrew'
        superuser = User.objects.filter(username=superuser_username).first()
        if superuser:
            superuser.first_name = 'Andrew'
            superuser.last_name = 'Smith'
            superuser.save()
            self.stdout.write(f"Updated superuser {superuser_username}")
        else:
            raise CommandError(f"Superuser {superuser_username} not found. Command aborted.")

        self.seed_users()
        self.seed_instructors()
        self.seed_home_images()
        self.seed_classes()

        self.stdout.write("Done seeding data.")


    def seed_users(self):
        if User.objects.count() < 2:
            User.objects.create(
                password='!IkXm0tGy0ENkHXrFqveuiRgAIrnWAondjHSkXCrY',
                username='Sophie',
                first_name='Sophie',
                last_name='Smith',
                email='sophiesmith@email.com',
                is_staff=True
            )
            self.stdout.write("Seeded Users.")
        else:
            self.stdout.write("Users already seeded.")


    def seed_instructors(self):
        if not Instructor.objects.exists():
            Instructor.objects.create(
                phone='07111222333',
                DOB=datetime.date(1980, 1, 1),
                image='instructors/Sophie.jpg',
                entry_code='HJA7A13E',
                instr_type='Nutrition Adviser',
                desc="Meet Sophie, the gym's expert Nutrition Consultant, whose holistic approach to diet and wellness sets her apart. With a background in nutritional science and a talent for crafting meal plans that are both delicious and nutritionally balanced, Sophie guides you through the maze of dietary choices. Her personalised consultations aim to harmonise your diet with your fitness goals, ensuring that your body receives the optimal fuel it needs to thrive.",
                qualifications=["Master's Degree in Sports Nutrition", "Level III Certificate in Workout Nutrition", "Certified Yoga Instructor"],
                activities=["Nutrition Consultations", "Yoga Classes", "Body Mind & Spirit Personal Training", "Pilates"],
                order=100,
                user_id=2
            )
            Instructor.objects.create(
                phone='07111222334',
                DOB=datetime.date(1985, 1, 1),
                image='instructors/Andrew.jpg',
                entry_code='HJA7A13F',
                instr_type='Group Exercise Coach',
                desc="Introducing Andrew, the charismatic Group Exercise Coordinator, who brings a vibrant energy to every class he leads. From high-intensity interval training to wacky spin classes, Andrew's diverse expertise allows him to cater to a wide range of interests and fitness levels. His ability to create a supportive and fun community atmosphere makes every session not just a workout, but an experience that keeps members coming back for more.",
                qualifications=["Gym Instructor Level III", "Spin Instruction Certificate", "Level II Gym Health & Safety"],
                activities=["HIIT Classes", "Spin Classes", "Body Pump Classes", "Swimming"],
                order=200,
                user_id=1
            )
            self.stdout.write("Seeded Instructors.")
        else:
            self.stdout.write("Instructors already seeded.")


    def seed_home_images(self):
        if not Image.objects.exists():
            Image.objects.create(
                image='home/home_1.jpg',
                desc='Elevate your well-being with state-of-the-art facilities designed to boost both physical and mental health.',
                order=100
            )
            Image.objects.create(
                image='home/home_2.jpg',
                desc='Join a vibrant community where fitness meets friendship, and every workout is a social event.',
                order=200
            )
            Image.objects.create(
                image='home/home_3.jpg',
                desc='Discover a variety of classes led by top-tier instructors, from heart-pumping HIIT to serene yoga sessions.',
                order=300,
                link_text='classes',
                link='classes'
            )
            Image.objects.create(
                image='home/home_4.jpeg',
                desc='Learn from the best: our certified instructors bring passion, expertise, and personalised guidance to every class.',
                order=400,
                link_text='team',
                link='instructors'
            )
            Image.objects.create(
                image='home/home_5.webp',
                desc='Flexible schedules that fit your life - early bird or night owl, or constantly busy, find your perfect workout time.',
                order=500,
                link_text='schedule',
                link='scheduled'
            )
            Image.objects.create(
                image='home/home_6.jpg',
                desc='Always evolving: We introduce new, popular classes regularly based on what our members love.',
                order=600
            )
            Image.objects.create(
                image='home/home_7.jpg',
                desc='Experience the future of fitness with our cutting-edge technology that tracks and enhances your progress.',
                order=700
            )
            Image.objects.create(
                image='home/home_8.jpg',
                desc='Beyond the workout: embrace a holistic approach to wellness with our wellness workshops and nutrition counselling.',
                order=800
            )
            self.stdout.write("Seeded Home Images.")
        else:
            self.stdout.write("Home Images already seeded.")
            

    def seed_classes(self):
        if not Class.objects.exists():
            Class.objects.create(
                name='Spin',
                image='classes/spin.jpg',
                desc='Pedal your way to fitness in our high-energy cycling classes, where heart-pumping music and motivating instructors propel you towards your fitness goals.',
                order=100,
                user_id=1
            )
            Class.objects.create(
                name='Yoga',
                image='classes/yoga.jpg',
                desc='Discover inner peace and outer strength with our diverse yoga classes, from energizing Vinyasa flows to calming Yin sessions.',
                order=600,
                user_id=1
            )
            Class.objects.create(
                name='Pilates',
                image='classes/pilates.jpg',
                desc='Sculpt your body and build core strength with our dynamic Pilates classes, designed to enhance flexibility and promote overall well-being.',
                order=500,
                user_id=1
            )
            Class.objects.create(
                name='Kickboxing',
                image='classes/kickboxing.jpg',
                desc="Unleash your inner fighter and torch calories with our empowering boxing and kickboxing classes, where you'll jab, hook, and kick your way to a stronger, leaner you.",
                order=400,
                user_id=1
            )
            Class.objects.create(
                name='CrossFit',
                image='classes/crossfit.jpg',
                desc='Join our CrossFit community and experience the ultimate in functional fitness, with intense workouts that will push you to new heights of strength, endurance, and performance.',
                order=800,
                user_id=1
            )
            Class.objects.create(
                name='Zumba',
                image='classes/zumba.webp',
                desc='Shake off stress and let loose with our exhilarating Zumba classes, where infectious rhythms and fun choreography make every workout feel like a dance party.',
                order=200,
                user_id=1
            )
            Class.objects.create(
                name='Boot Camp',
                image='classes/boot_camp.jpeg',
                desc='Ignite your metabolism and push your limits with our challenging Boot Camp classes, blending cardio, strength, and teamwork for a full-body burn.',
                order=300,
                user_id=1
            )
            Class.objects.create(
                name='Body Pump',
                image='classes/body_pump.jpg',
                desc='Pump up your strength and confidence with our Body Pump classes, using barbells and high-repetition exercises to sculpt muscles and boost metabolism.',
                order=700,
                user_id=1
            )
            self.stdout.write("Seeded Classes.")
        else:
            self.stdout.write("Classes already seeded.")
