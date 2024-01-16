from transformers import pipeline
from transformers import MBartTokenizer, MBartForConditionalGeneration
tokenizer = MBartTokenizer.from_pretrained("ARTeLab/mbart-summarization-fanpage")
model = MBartForConditionalGeneration.from_pretrained("ARTeLab/mbart-summarization-fanpage")


classifier = pipeline("summarization", model = model, tokenizer = tokenizer)


res = classifier("""
                 La torre degli Asinelli è una delle cosiddette due torri di Bologna, simbolo della città, 
                 situate in piazza di porta Ravegnana, all'incrocio tra le antiche strade San Donato 
                 (ora via Zamboni), San Vitale, Maggiore e Castiglione. Eretta, secondo la tradizione, 
                 fra il 1109 e il 1119 dal nobile Gherardo Asinelli, la torre è alta 97,20 metri, pende 
                 verso ovest per 2,23 metri e presenta all'interno una scalinata composta da 498 gradini. 
                 Ancora non si può dire con certezza quando e da chi fu costruita la torre degli Asinelli. 
                 Si presume che la torre debba il proprio nome a Gherardo Asinelli, il nobile cavaliere di 
                 fazione ghibellina al quale se ne attribuisce la costruzione, iniziata secondo una consolidata 
                 tradizione l'11 ottobre 1109 e terminata dieci anni dopo, nel 1119.
                 """)

print(res)


# La torre degli Asinelli è alta 97,20 metri, pende verso ovest per 2,23 metri e presenta all’interno una scalinata 
# composta da 498 gradini. Ancora non si può dire con certezza quando e da chi fu costruita la torre degli Asinelli, 
# si presume che debba il proprio nome a Gherardo Asinelli, il nobile cavaliere di fazione ghibellina al quale se ne 
# attribuisce la costruzione, iniziata secondo una consolidata tradizione l’11 ottobre 1109 e terminata dieci anni 
# dopo, nel 1119.

