from abc import ABC, abstractmethod


class ActionsParent(ABC):

    @abstractmethod
    def launch_app(self):
        pass


    @abstractmethod
    def enter_text(self):
        pass
    
    @abstractmethod
    def is_element_displayed(self, *args):
        pass
    
    @abstractmethod
    def wait_for_element(self, *args):
        pass
    
    @abstractmethod
    def click_button(self, *args):
        pass

    @abstractmethod
    def fluentWaitNew(self, *args):
        pass
    
    @abstractmethod
    def screenshotAttachment(self, Screenshot):
        pass

    