import dspy

class ChatSignature(dspy.Signature):
    """Answer questions using conversation history for context."""
    question: str = dspy.InputField(desc="The current question from the user")
    history: dspy.History = dspy.InputField(desc="Previous conversation messages")

    answer: str = dspy.OutputField(desc="Answer that takes conversation history into account")

class ChatModule(dspy.Module):
    """
    ChatModule is used to generate an chat like interface using DSPy.
    """
    def __init__(self,):
        self.qa = dspy.Predict(ChatSignature)
        self._history = dspy.History(messages=[])

    def _ask(self, question: str, **kwargs):
        result = self.qa(question=question, history=self._history, **kwargs)

        if result.answer is None:
            raise ValueError("The model did not return an answer. Please check the model configuration and input parameters.")
        # Append the question and answer to the history
        if not isinstance(result.answer, str):
            raise TypeError(f"Expected answer to be a string, but got {type(result.answer)}. Please check the model output.")
        
        self._history.messages.append({"question": f"User: {question}", "answer": f"Assistant: {result.answer}"})

        return dspy.Prediction(
            answer=result.answer,
        )
    
    def forward(self, question: str, **kwargs):
        """
        Forward method to handle synchronous question answering.
        Args:
            question (str): The question to ask.
            **kwargs: Additional keyword arguments for the model.
        Returns:
            dspy.Prediction: The prediction result containing the answer.
        """
        return self._ask(question, **kwargs)

    def _aforward(self, question: str, **kwargs):
        """
        Forward method to handle asynchronous question answering.
        Args:
            question (str): The question to ask.
            **kwargs: Additional keyword arguments for the model.
        Returns:        
            dspy.Prediction: The prediction result containing the answer.
        """
        return self._ask(question, **kwargs)