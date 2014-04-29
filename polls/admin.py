from django.contrib import admin
from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    # Show specific fields of the object in the Admin site
    list_display = ('question', 'pub_date', 'was_published_recently')
    # Add side bar filter for date
    list_filter = ['pub_date']
    # And a search field, by question
    search_fields = ['question']
    # This will separate fields in different sets in the Admin page
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Poll, PollAdmin)

