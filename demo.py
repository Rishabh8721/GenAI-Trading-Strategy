from process import gen_ai_model
import warnings

# Ignore the specific FutureWarning related to Series.__getitem__ treating keys as positions
warnings.filterwarnings("ignore", category=FutureWarning)

company_name = "Clearwater Analytics"
symbol = "CWAN"

analysis = gen_ai_model.get_initial_analysis(company_name, symbol, False)
print(analysis)

question = gen_ai_model.follow_up_question("Conclude news.")
print(question)