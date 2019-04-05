import os

board_bitstream_dict = {
		'U200' : 'u200.xclbin',
		'Ultra96' : 'ultra96.xclbin'
	}

_board = os.environ.get('BOARD', 'BOARD_ENV_NOT_SET')
_bitstream_file = board_bitstream_dict.get(_board, 'BOARD_NOT_FOUND')

dir = os.path.dirname(__file__)
BITSTREAM = os.path.join(dir, _bitstream_file)




