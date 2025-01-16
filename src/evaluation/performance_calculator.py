from translatepy import Translator
class PerformanceCalculator:
    count_instances = 0
    correct_instances = 0 
    
    @classmethod
    def calculate(cls, eval_response, language):
        translate = Translator()
        try:
            translated = translate.translate("CORRETO", destination_language=language)
            term_exit = translated.result
        except Exception as e:
            print(f"Error trying to translate: {e}")
            return "Error translating text."
        
        cls.count_instances = 0
        cls.correct_instances = 0

        for value in eval_response:
            for eval in value:
                cls.count_instances += 1
                if eval == term_exit:
                    cls.correct_instances += 1

        if cls.count_instances == 0:
            return 0 
        return (cls.correct_instances / cls.count_instances) * 100
        
