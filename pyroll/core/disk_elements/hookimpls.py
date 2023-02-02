from .disk_element_unit import DiskElementUnit


@DiskElementUnit.disk_element_count
def no_disks(self: DiskElementUnit):
    return 0


@DiskElementUnit.DiskElement.duration
def disk_duration(self: DiskElementUnit.DiskElement):
    return self.parent.duration / self.parent.disk_element_count


@DiskElementUnit.DiskElement.length
def disk_length(self: DiskElementUnit.DiskElement):
    return self.parent.length / self.parent.disk_element_count


@DiskElementUnit.DiskElement.InProfile.x
def in_x(self: DiskElementUnit.DiskElement.InProfile):
    # for first disk: get from parent in_profile
    if self.disk_element is self.disk_element.parent.disk_elements[0]:
        return self.disk_element.parent.in_profile.x

    # else: get from prev disk
    return self.disk_element.prev.out_profile.x
