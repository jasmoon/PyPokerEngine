from tests.base_unittest import BaseUnitTest
from pypokerengine.players.sample.console_player import PokerPlayer as ConsolePlayer

class ConsolePlayerTest(BaseUnitTest):

  def setUp(self):
    self.valid_actions = [\
        {'action': 'fold', 'amount': 0},\
        {'action': 'call', 'amount': 10},\
        {'action': 'raise', 'amount': {'max': 105, 'min': 15}}\
    ]

  def test_declare_fold(self):
    mock_input = self.__gen_raw_input_mock(['f'])
    player = ConsolePlayer(mock_input)
    action, amount = player.declare_action(None, self.valid_actions, None, None)
    self.eq('fold', action)
    self.eq(0, amount)

  def test_declare_call(self):
    mock_input = self.__gen_raw_input_mock(['c'])
    player = ConsolePlayer(mock_input)
    action, amount = player.declare_action(None, self.valid_actions, None, None)
    self.eq('call', action)
    self.eq(10, amount)

  def test_declare_valid_raise(self):
    mock_input = self.__gen_raw_input_mock(['r', '15'])
    player = ConsolePlayer(mock_input)
    action, amount = player.declare_action(None, self.valid_actions, None, None)
    self.eq('raise', action)
    self.eq(15, amount)

  def test_correct_invalid_raise(self):
    mock_input = self.__gen_raw_input_mock(['r', '14', '105'])
    player = ConsolePlayer(mock_input)
    action, amount = player.declare_action(None, self.valid_actions, None, None)
    self.eq('raise', action)
    self.eq(105, amount)


  def __gen_raw_input_mock(self, mock_returns):
    counter = []
    def raw_input_wrapper(self):
      mock_return = mock_returns[len(counter)]
      counter.append(0)
      return mock_return
    return raw_input_wrapper