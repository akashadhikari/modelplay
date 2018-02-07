# class CachedModel(models.Model):
#
#     def update_cache(cls):
#
#     # UPDATE CACHE
#
#     def delete(self):
#         self.update_cache()
#         super().delete()
#
#     def save(self, *args, **kwargs):
#         self.update_cache()
#         super().delete(*args, **kwargs)
#
#
# class Group(CachedModel):
#     name = models.CharField(max_length=60)
#
#
# class ContactPerson(models.Model):
#     pass
#
# class Reminder(models.Model):
#     datetime = models.DateTimeField()
#     remarks = models.TextField()
#
#
# MEDIUMS = (
#     ('Outbound Call', 'Outbound Call'),
#     ('Inbound Call', 'Inbound Call'),
#     ('Inbound Call', 'Inbound Call'),
# )
#
#
# class Stage(CachedModel):
#     name = models.CharField(max_length=60)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     enable_reminder= models.BooleanField(default=False)
#     fields = JSONField()
#
#
# class Communication(models.Model):
#     client = models.ForeignKey(Client)
#     lead = models.ForeignKey(User)
#     date_time = models.DateTimeField()
#     medium = models.CharField(choices=MEDIUMS)
#     contact = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)
#     # stage_log = models.ForeignKey(StageLog, on_delete=models.CASCADE)
#     stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
#     values = JSONField()
#     reminder = models.ForeignKey(Reminder)