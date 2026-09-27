from rest_framework.throttling import UserRateThrottle


class TenMinutesThrottle(UserRateThrottle):
    scope = 'ten'


class FiftyMinuteThrottle(UserRateThrottle):
    scope = 'fifty'