class CampaignChannel:
    EMAIL = 'email'
    WHATSAPP = 'whatsapp'
    CHOICES = [
        (EMAIL, 'Email'),
        (WHATSAPP, 'WhatsApp'),
    ]

class CampaignStatus:
    FAILED = 'failed'
    TRIGERRED = 'trigerred'
    EXEC = 'executed'
    PENDING = 'pending'

    CHOICES = [
        (FAILED, 'Failed'),
        (TRIGERRED, 'Trigerred'),
        (PENDING, 'Pending'),
    ]


class LogsStatus:
    FAILED = 'failed'
    SUCCSESS = 'success'

    CHOICES = [
        (FAILED, 'Failed'),
        (SUCCSESS, 'Success')
    ]
