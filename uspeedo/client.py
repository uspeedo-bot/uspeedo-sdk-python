"""
Copyright 2023 USpeedo Technology Co., Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from uspeedo.core import client


class Client(client.Client):
    def __init__(self, config: dict, transport=None, middleware=None):
        self._config = config
        super(Client, self).__init__(config, transport, middleware)
    
    def email(self):
        from uspeedo.services.email.client import EmailClient

        return EmailClient(
            self._config, self.transport, self.middleware, self.logger
        )
    
    def whatsapp(self):
        from uspeedo.services.whatsapp.client import WhatsAppClient

        return WhatsAppClient(
            self._config, self.transport, self.middleware, self.logger
        )
