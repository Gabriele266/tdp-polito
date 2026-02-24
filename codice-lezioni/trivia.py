import random

class Player:
    def __init__(self, nickname: str):
        self.nickname = nickname

    def write_result(self, level: int, filename: str) -> None:
        try:
            file = open(filename, "a")
            file.write(f"{self.nickname} {level}\n")
            file.close()
        except FileNotFoundError:
            print(f"Unable to open file {filename}")

class Question:
    def __init__(self, text: str, difficulty:int, correct_answer: str, other_answers: list[str]):
        self.text = text
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.other_answers = other_answers


    def has_same_difficulty(self, other) -> bool:
        return self.difficulty == other.difficulty

    def check_correct(self, answer_number: int, all_options: list[str]) -> bool:
        """Check if the given answer number is correct for the given options"""
        return answer_number == all_options.index(self.correct_answer)

    def present_questions(self) -> list[str]:
        """Get an array with all the answers shuffled randomically"""
        q = [self.correct_answer, *self.other_answers]
        random.shuffle(q)
        return q

    def equals(self, other) -> bool:
        return self.text == other.text

    @classmethod
    def read_chunk(cls, lines: list[str]):
        """Read a chunk of lines and converto to a question"""
        t = lines[0]
        dif = int(lines[1])
        cor = lines[2]
        other_answers = lines[3:]

        return cls(t, difficulty=dif, correct_answer=cor, other_answers=other_answers)

    def print_question(self) -> list[str]:
        print(self.text)
        print(f"Difficulty: {self.difficulty}")
        r = self.present_questions()
        l = 0
        for a in r:
            print(f"{l}) {a}")
            l += 1

        return r

class QuestionListHelper:
    def __init__(self, question_list: list[Question]):
        self.question_list = question_list

    def __remove_question__(self, title: str):
        for q in self.question_list:
            if q.text == title:
                self.question_list.remove(q)

    def __filter_by_difficulty__(self, difficulty: int) -> list[Question]:
        return list(filter(lambda q: q.difficulty == difficulty, self.question_list))

    def get_random_question(self, difficulty: int) -> Question:
        """Get the random question from the list, ensuring that the question has not been presented before"""
        dif = self.__filter_by_difficulty__(difficulty)    # all questions with the given difficulty
        i = random.randint(0, len(dif) - 1)
        q = dif[i]
        self.__remove_question__(q.text)
        return q

    def has_available_questions(self, difficulty: int) -> bool:
        return len(self.__filter_by_difficulty__(difficulty)) > 0

class FileQuestionLoader:
    def __init__(self, filename: str):
        """Create a new question loader to work from a specific file
        {filename} path to the text file
        """

        self.filename = filename

    def load(self) -> list[Question]:
        """Load all the questions from the file or return an empty list"""
        try:
            file = open(self.filename)
            questions = []
            line = file.readline()

            while line != "":
                ch = []     # File chunk

                while line != "\n" and len(ch) <= 6:
                    ch.append(line)
                    line = file.readline()

                questions.append(Question.read_chunk(ch))
                ch = []
                line = file.readline()

            file.close()
            return questions

        except FileNotFoundError:
            print(f"Unable to open file {self.filename}")
            return []

# main
print("Start")
loader = FileQuestionLoader("input.txt")
questions: list[Question] = loader.load()         # load all the questions
helper = QuestionListHelper(questions)
print(f"Loaded {len(questions)} questions")
print("Welcome to trivia game")
player = Player("foo")

level = 0
while helper.has_available_questions(level):
    q = helper.get_random_question(difficulty=level)

    answer_list = q.print_question()
    answer_num = int(input("Insert your answer here --> "))
    if q.check_correct(answer_num, answer_list):
        level += 1
    else:
        print("Wrong answer")
        break

print(f"Final score: {level}")
p = Player(input("Inserisci il tuo nickname: "))
p.write_result(level, "results.txt")