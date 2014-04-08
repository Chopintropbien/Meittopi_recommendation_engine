__author__ = 'andrei'


class GenericFormatter(object):

    def __init__(self, field_names, types, example):
        """

        :param field_names:
        :param types:
        :param example:
        """
        self.field_names = field_names
        self.types = types
        self.example = example

    def get_sample(self):
        """
        Gets the sample of the object managed by the formatter

        :return:
        """
        return dict(zip(self.field_names, self.example))

    def verify(self, format_dict):
        """
        checks that the provided dict conforms well to the formatter rules

        :param format_dict:
        :return:
        """
        type_dict = dict(zip(self.field_names, self.types))
        if format_dict.keys() != type_dict.keys():
            return False
        return all(type(val) == type_dict[key] for key, val in format_dict.iteritems())


class ListFormatter(object):

    def __init__(self, generic_name, simple_formatter, limiter=None):
        """

        :param generic_name:
        :param simple_formatter:
        """
        self.generic_name = generic_name
        self.generic_formatter = simple_formatter
        self.limiter = limiter

    def get_sample(self):
        """
        Recovers a sample

        :return:
        """
        return {self.generic_name + '_0': self.generic_formatter.get_sample()}

    def verify(self, list_dict):
        """
        Verifies that the provided dict is formatted correctly

        :param list_dict:
        :return:
        """
        if self.limiter:
            if self.limiter < len(list_dict):
                return False
        try:
            if not all((self.generic_name == key.split('_')[0] and int(key.split('_')[1] >= 0)
                            for key in list_dict.iterkeys())):
                return False
        except TypeError:
            return False
        return all(self.generic_formatter.verify(val) for val in list_dict.itervalues())


Composite_formatter


class CompositeFormatter(object):

    def __init__(self, field_names, types, example):
        self.field_names= field_names,
        self.types= types
        self.example = example # TODO: build here to integrate default examples from the

    def get_sample(self):
        pass

    def verify(self, composite_dict):
        pass


Friend = GenericFormatter(field_names=['photo', 'pseudo', 'city', 'revue_number', 'unique_id'],
                                     types=[str, str, str, int, str],
                                     example=['Andreis_photo_hash', 'Andrei Kucharavy', 'Kansas City', 3, 'qfjk'])

Compliment = GenericFormatter(field_names=['photo', 'pseudo', 'date', 'compiment_contents', 'referenced restaurant', 'unique_id','review', 'restaurant'],
                                         types=[str, str, str, int, str],
                                         example=['Profile_test_hash', 'Andrei Kucharavy', 'Kansas City', 3, 'qfjk'])

Invitee = GenericFormatter(field_names=['photo', 'name', 'confirmed_venue', 'unique_id'],
                           types=[str, str, bool, str],
                           example=['Andreis_photo_hash', 'Andrei Kucharavy', True, 'qfjk'])

Photo = GenericFormatter(field_names=['photo'],
                         types=[str],
                         example=['Andreis_photo_hash'])

photo_list = ListFormatter('photo',Photo, 3)

Invitee_list = ListFormatter('invitee', Invitee)

Event = CompositeFormatter(field_names=['organiser_name', 'organiser_photo', 'photo_list', 'event_title', 'creation_date',
                                      'event_date', 'invitees_list', 'personal_message', 'description', 'organisor_id',
                                      'event_id'],
                            types = [],
                            example = [])




friends_list_formatter = ListFormatter('friend', Friend)


def expose_API():
    #TODO
    pass

if __name__ == "__main__":
    print Friend.get_sample()
    print Friend.verify(Friend.get_sample())

    print friends_list_formatter.get_sample()
    print friends_list_formatter.verify(friends_list_formatter.get_sample())