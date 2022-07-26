import requests


class XenForoAPI:
    def __init__(self, key: str, baseUrl: str) -> None:
        """
        :param key: api key created in ACP.
        :param baseUrl: example -> https://mydomain.com/api/
        """
        self.api_key = key
        self.baseUrl = baseUrl
        self.headers = {
            'XF-Api-Key': self.api_key
        }
        self.session = requests.session()

    def get(self, endpoint):
        return self.session.get(self.baseUrl + endpoint, headers=self.headers).json()

    def post(self, endpoint, data=None):
        return self.session.post(self.baseUrl + endpoint, headers=self.headers, data=data).json()

    def delete(self, endpoint, data=None):
        return self.session.delete(self.baseUrl + endpoint, headers=self.headers, data=data).json()

    def getMe(self) -> dict:
        """
        :return: information about the current API user
        """
        return self.get('me')

    def getAlerts(self) -> dict:
        """
        :return: the API user's list of alerts
        """
        return self.get('alerts')

    def getConversations(self) -> dict:
        """
        :return: the API user's list of conversations.
        """
        return self.get('conversations')

    def getNodes(self) -> dict:
        """
        :return: the node tree.
        """
        return self.get('nodes')

    def getPost(self, post_id: int = None) -> dict:
        """
        :return: information about the specified post
        """
        if post_id is None:
            raise Exception('Parameter post_id is required.')

        return self.get(f'posts/{post_id}')

    def getNode(self, node_id: int = None) -> dict:
        """
        :return: information about the specified node
        """
        if node_id is None:
            raise Exception('Parameter node_id is required')

        return self.get(f'nodes/{node_id}')

    def getProfilePostComment(self, comment_id: int = None) -> dict:
        """
        :return: information about the specified profile post comment.
        """
        if comment_id is None:
            raise Exception('Parameter comment_id is required')

        return self.get(f'profile-post-comments/{comment_id}')

    def getForum(self, forum_id: int = None) -> dict:
        """
        :return: information about the specified forum
        """
        if forum_id is None:
            raise Exception('Parameter forum_id is required')

        return self.get(f'forums/{forum_id}')

    def deletePost(self,
                   post_id: int = None,
                   hard_delete: bool = False,
                   reason: str = '',
                   author_alert: bool = False,
                   author_alert_reason: str = '') -> dict:
        """
        :return: Deletes the specified post. Default to soft deletion.
        """
        if post_id is None:
            raise Exception('Parameter post_id is required.')

        return self.delete(f'posts/{post_id}', {
            'hard_delete': hard_delete,
            'reason': reason,
            'author_alert': author_alert,
            'author_alert_reason': author_alert_reason
        })

    def getConversationMessage(self, message_id: int = None) -> dict:
        """
        :return: The specified conversation message.
        """
        if message_id is None:
            raise Exception('Parameter message_id is required.')

        return self.get(f'conversation-messages/{message_id}')

    def replyToConversation(self,
                            conversation_id: int = None,
                            message: str = None,
                            attachment_key: str = '') -> dict:
        """
        :return: Replies to a conversation
        """
        if conversation_id is None:
            raise Exception('Parameter conversation_id is required.')

        if message is None:
            raise Exception('Parameter message is required.')

        return self.post(f'conversation-messages', {
            'conversation_id': conversation_id,
            'message': message,
            'attachment_key': attachment_key
        })

