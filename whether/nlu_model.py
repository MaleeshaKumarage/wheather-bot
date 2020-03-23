from rasa.nlu.training_data import load_data
from rasa.nlu import config
from rasa.nlu.model import Trainer, Metadata, Interpreter

def train_nlu(data, configuration, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configuration))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'whethernlu')

def run_nlu():
    interpreter = Interpreter.load('./models/nlu/whethernlu')
    print(interpreter.parse(u"I am planning my holiday in Barcelona. I wonder what is the whether out there"))

if __name__ == "__main__":
    #train_nlu('./data/data.json','config_spacy.json', './models/nlu')
    run_nlu()
