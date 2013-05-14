import oxford_term_dates

from moxie.core.service import Service


class DatesService(Service):
    """Service to provide various methods to access dates particular to University of Oxford,
    such as term dates.
    """

    def get_formatted_date(self, components):
        """Returns today's date with the name of the term.
        :param components: components to format
        """
        return oxford_term_dates.format(components)

    def get_today_components(self):
        """Returns today's date components (week number, term short/long)
        """
        return oxford_term_dates.ox_date_dict()

    def get_ox_components(self, datetime):
        """Returns date components for an arbitrary date
        :param datetime: datetime object
        :return: components for this date
        """
        return oxford_term_dates.ox_date_dict(datetime)