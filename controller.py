import model_mult
import view
import Model_adition




def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    Model_adition.init(value_a, value_b)
    result = Model_adition.sum()
    view.view_data(result)
