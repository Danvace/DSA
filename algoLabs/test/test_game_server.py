import unittest

from algoLabs.src.game_server import best_server_place, parse_data_from_file


class Test(unittest.TestCase):

    def test_gameserver1(self):
        adjacency_list, client_nodes = parse_data_from_file("gamsrv.in")
        res = best_server_place(adjacency_list, client_nodes)
        self.assertEqual((100, 4), res)

    def test_gameserver2(self):
        adjacency_list, client_nodes = parse_data_from_file("gamsrv2.in")
        res = best_server_place(adjacency_list, client_nodes)
        self.assertEqual((10, 5), res)

    def test_gameserver3(self):
        adjacency_list, client_nodes = parse_data_from_file("gamsrv3.in")
        res = best_server_place(adjacency_list, client_nodes)
        self.assertEqual((1000000000, 2), res)
