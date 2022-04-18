class FeedbackModel:
    def __init__(self, file_id: str, file_name: str):
        self.FileId = file_id
        self.FileName = file_name
        self.QuestionIds = []

    def add_question_id(self, question_id: str):
        self.QuestionIds.append(question_id)