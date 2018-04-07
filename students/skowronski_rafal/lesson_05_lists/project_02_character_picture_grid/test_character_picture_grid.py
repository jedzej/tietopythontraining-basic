from character_picture_grid import get_character_image


class TestCharacterPictureGrid():
    def test_get_character_image(self):
        expected = '..OO.OO..\n.OOOOOOO.\n.OOOOOOO.\n..OOOOO..\n' + \
            '...OOO...\n....O....\n'

        assert get_character_image() == expected
