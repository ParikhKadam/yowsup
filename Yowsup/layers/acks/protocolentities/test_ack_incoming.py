from .ack_incoming import IncomingAckProtocolEntity
from .test_ack import AckProtocolEntityTest
from Yowsup.structs import ProtocolTreeNode

class IncomingAckProtocolEntityTest(AckProtocolEntityTest):
    def setUp(self):
        super(IncomingAckProtocolEntityTest, self).setUp()
        self.ProtocolEntity = IncomingAckProtocolEntity
        self.node.setAttribute("from", "ack_from")
        self.node.setAttribute("t", "ack_timestamp")
