from .GedcomIndividual import GedcomIndividual


class ancestor_graph_individual():
    """
    Class which represents one appearance of an individual
    """
    # x positions in different family appearances
    _x_position = None
    visible_parent_family = None
    # color of this individual
    color = [200, 200, 255]
    # tuple: child individual where this individual was placed, family where that child individual is child
    visual_placement_child = None
    # ordinal value of the birth date
    __birth_date_ov = None
    # ordinal value of the death date
    __death_date_ov = None

    def __init__(self, instances, individual_id, distance):
        self._distance = distance
        self.items = []
        self.individual_id = individual_id
        self.__instances = instances
        self.individual = self.__instances[('i', self.individual_id)]
        self.individual.graphical_representations.append(self)
        pass

    def get_marriages(self):
        marriages = self.individual.marriages
        return [m.graphical_representations[0] for m in marriages if m.has_graphical_representation()]

    def get_width(self, family, recursive=False):
        x_min, x_max = self.get_range(family)
        width = x_max - x_min + 1
        return width

    def get_range(self, family):
        family_id = None
        if family is not None:
            family_id = family.family_id
        if (self.individual_id, family_id) in self.__instances.width_cache:
            return self.__instances.width_cache[(self.individual_id, family_id)]
        width = 0
        child_of_family = self.visible_parent_family
        # spouse_placement_family_id = self.visual_placement_child[0].graphical_representations[0].visible_parent_family.family_id
        # spouse_placement_family = self.visual_placement_child[0].graphical_representations[0].visible_parent_family
        # if self.visible_parent_family and False:# and family_id == self.visible_parent_family.family_id:
        #     width += len(self.visible_parent_family.visible_children)
        #     x_v = [c[2].graphical_representations[0].get_x_position()[self.visible_parent_family.family_id][1] for c_id, c in self.visible_parent_family.visible_children.items()]
        # el
        if family_id in self.x_position:
            x_v = [self._x_position[family_id][1]]
        # else:
        #     x_v = [self._x_position[spouse_placement_family_id][1]]
        x_min = x_v.copy()
        x_max = x_v.copy()
        i = 1 if self._x_position[list(self._x_position.keys())[0]][3] else 0
        if child_of_family and list(self._x_position.keys())[i] == family_id and list(self._x_position.values())[0][1]==list(self._x_position.values())[i][1]:
            father, mother = child_of_family.family.get_husband_and_wife()
            if father and father.has_graphical_representation():
                f_x_positions = father.graphical_representations[0].get_x_position()
                i = 1 if f_x_positions[list(f_x_positions.keys())[0]][3] else 0
                if list(f_x_positions.keys())[i] == child_of_family.family_id:
                    f_x_min, f_x_max = father.graphical_representations[0].get_range(
                        child_of_family)
                    x_min.append(f_x_min)
                    x_max.append(f_x_max)
                else:
                    x_pos = father.graphical_representations[0].get_x_position()[child_of_family.family_id][1]
                    x_min.append(x_pos)
                    x_max.append(x_pos)
            if mother and mother.has_graphical_representation():
                m_x_positions = mother.graphical_representations[0].get_x_position()
                i = 1 if m_x_positions[list(m_x_positions.keys())[0]][3] else 0
                if list(m_x_positions.keys())[i] == child_of_family.family_id:
                    m_x_min, m_x_max = mother.graphical_representations[0].get_range(
                        child_of_family)
                    x_min.append(m_x_min)
                    x_max.append(m_x_max)
                else:
                    x_pos = mother.graphical_representations[0].get_x_position()[child_of_family.family_id][1]
                    x_min.append(x_pos)
                    x_max.append(x_pos)
            # add siblings
            x_v = [c[2].graphical_representations[0].get_x_position()[self.visible_parent_family.family_id][1] for c_id, c in self.visible_parent_family.visible_children.items()
                        if self.visible_parent_family.family_id in c[2].graphical_representations[0].get_x_position()]
            x_min += x_v
            x_max += x_v
        x_min = min(x_min)
        x_max = max(x_max)
        self.__instances.width_cache[(self.individual_id, family_id)] = x_min, x_max
        return x_min, x_max

    def __get_name(self):
        return self.individual.name
    name = property(__get_name)

    def __get_birth_date(self):
        if self.individual.events['birth_or_christening']:
            return self.individual.events['birth_or_christening']['date'].date().strftime('%d.%m.%Y')
        else:
            return None
    birth_date = property(__get_birth_date)

    def __get_death_date(self):
        if self.individual.events['death_or_burial']:
            return self.individual.events['death_or_burial']['date'].date().strftime('%d.%m.%Y')
        else:
            return None
    death_date = property(__get_death_date)

    def get_x_position(self):
        return self._x_position

    def set_x_position(self, x_position, family, parent_starting_point=False):
        # self._x_position = x_position
        # return
        if family:
            family_id = family.family_id
            if family.marriage:
                ov = family.marriage['ordinal_value']
            else:
                ov = 0
        else:
            family_id = None
            ov = 0
        if not self._x_position:
            self._x_position = {}
        if family_id not in self._x_position:
            self._x_position[family_id] = (
                (ov, x_position, family, parent_starting_point))
        _x_position = {}
        if None in self._x_position:
            _x_position[None] = self._x_position[None]
        _x_position.update(dict(sorted([i for i in self._x_position.items() if i[0] is not None], key=lambda t: t[1])))
        self._x_position = _x_position

    x_position = property(get_x_position, set_x_position)

    def get_birth_event(self):
        return self.individual.events['birth_or_christening']

    def get_death_event(self):
        return self.individual.events['death_or_burial']

    def get_birth_date_ov(self):
        """
        get the ordinal value of the birth (or christening or baptism) date

        Returns:
            float: ordinal value of birth date
        """
        if self.__birth_date_ov is None:
            boc = self.individual.events.get('birth_or_christening')
            if boc:
                self.__birth_date_ov = boc['date'].date().toordinal()
                return self.__birth_date_ov
            return None
        else:
            return self.__birth_date_ov

    def get_death_date_ov(self):
        """
        get the ordinal value of the death (or burial) date

        Returns:
            float: ordinal value of death date
        """
        if self.__death_date_ov is None:
            dob = self.individual.events.get('death_or_burial')
            if dob:
                self.__death_date_ov = dob['date'].date().toordinal()
                return self.__death_date_ov
            return None
        else:
            return self.__death_date_ov

    def __get_birth_label(self):
        return self.individual.birth_label
    birth_label = property(__get_birth_label)

    def __get_death_label(self):
        string = self.individual.death_label
        if len(self._x_position) > 2 or len(self._x_position) == 2 and list(self._x_position.values())[0][1] != list(self._x_position.values())[1][1]:
            string += ' ' + " ".join(self.name)
        return string
    death_label = property(__get_death_label)

    def __get_children(self):
        return self.individual.children
    children = property(__get_children)
