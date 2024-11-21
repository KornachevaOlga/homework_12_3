import unittest
import inspect
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        peshehod = Runner('Пешеход')
        for i in range(10):
            peshehod.walk()
        self.assertEqual(peshehod.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        begun = Runner('Бегун')
        for i in range(10):
            begun.run()
        self.assertEqual(begun.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        peshehod = Runner('Пешеход')
        begun = Runner('Бегун')
        for i in range(10):
            peshehod.walk()
            begun.run()
        self.assertNotEqual(peshehod.distance, begun.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            #print()
            print(f'{test}:')
            print({k: str(v) for k, v in cls.all_results[test].items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_nik(self):
        tour = Tournament(90, self.usain, self.nik)
        results = tour.start()
        self.__class__.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_nik(self):
        tour = Tournament(90, self.andrey, self.nik)
        results = tour.start()
        self.__class__.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_nik(self):
        tour = Tournament(90, self.usain, self.andrey, self.nik)
        results = tour.start()
        self.__class__.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)


if __name__ == '__main__':
    unittest.main()
# import unittest
# from runner_and_tournament import Runner, Tournament
#
#
# class RunnerTest(unittest.TestCase):
#     is_frozen = False
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_walk(self):
#         peshehod = Runner('Пешеход')
#         for i in range(10):
#             peshehod.walk()
#         self.assertEqual(peshehod.distance, 50)
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_run(self):
#         begun = Runner('Бегун')
#         for i in range(10):
#             begun.run()
#         self.assertEqual(begun.distance, 100)
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_challenge(self):
#         peshehod = Runner('Пешеход')
#         begun = Runner('Бегун')
#         for i in range(10):
#             peshehod.walk()
#             begun.run()
#         self.assertNotEqual(peshehod.distance, begun.distance)
#
#
# class TournamentTest(unittest.TestCase):
#     is_frozen = False
#     @classmethod
#     def setUpClass(cls):
#         cls.all_results = []
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def setUp(self):
#         self.first = Runner('Усэйн', 10)
#         self.second = Runner('Андрей', 9)
#         self.third = Runner('Ник', 3)
#         # vs = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
#         # self.runners = {n: Runner(name=n, speed=v) for n, v in vs.items()} #
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_tournament(self):
#         tour = Tournament(90, self.first, self.third)
#         results = tour.start()
#         Tournament.all_results.append(results)
#         self.assertTrue(results[2] =='Ник')
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_tournament_2(self):
#         tour = Tournament(90, self.second, self.third)
#         results = tour.start()
#         Tournament.all_results.append(results)
#         self.assertTrue(results[2]=='Ник') # индекс 2- это значение? А значение это что и где указано
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_tournament_3(self):
#         tour = Tournament(90, self.first, self.second, self.third)
#         results = tour.start()
#         Tournament.all_results.append(results)
#         self.assertTrue(results[3]=='Ник')
#
#
#
#     @classmethod # обновиться все результаты после проверки?
#     def tearDownClass(cls):
#         for k, v in enumerate(cls.all_results):
#             print(f'{k+1}: {v}')
# import unittest
# from runner_and_tournament import Runner, Tournament
#
#
# class RunnerTest(unittest.TestCase):
#     is_frozen = False
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_walk(self):
#         peshehod = Runner('Пешеход')
#         for i in range(10):
#             peshehod.walk()
#         self.assertEqual(peshehod.distance, 50)
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_run(self):
#         begun = Runner('Бегун')
#         for i in range(10):
#             begun.run()
#         self.assertEqual(begun.distance, 100)
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_challenge(self):
#         peshehod = Runner('Пешеход')
#         begun = Runner('Бегун')
#         for i in range(10):
#             peshehod.walk()
#             begun.run()
#         self.assertNotEqual(peshehod.distance, begun.distance)
#
#
# class TournamentTest(unittest.TestCase):
#     is_frozen = False
#     @classmethod
#     def setUpClass(cls):
#         cls.all_results = {}
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def setUp(self):
#         self.first = Runner('Усэйн', 10)
#         self.second = Runner('Андрей', 9)
#         self.third = Runner('Ник', 3)
#         # vs = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
#         # self.runners = {n: Runner(name=n, speed=v) for n, v in vs.items()} #
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_tournament(self):
#         tour = Tournament(90, self.first, self.third)
#         results = tour.start()
#         TournamentTest.all_results[1]=results
#         self.assertTrue(results[2] =='Ник')
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_tournament_2(self):
#         tour = Tournament(90, self.second, self.third)
#         results = tour.start()
#         TournamentTest.all_results[2]=results
#         self.assertTrue(results[2]=='Ник') # индекс 2- это значение? А значение это что и где указано
#
#     @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
#     def test_tournament_3(self):
#         tour = Tournament(90, self.first, self.second, self.third)
#         results = tour.start()
#         TournamentTest.all_results[3]=results
#         self.assertTrue(results[3]=='Ник')
#
#
#
#     @classmethod # обновиться все результаты после проверки?
#     def tearDownClass(cls):
#         for k, v in cls.all_results.items():
#             print(f'{k+1}: {v}')
