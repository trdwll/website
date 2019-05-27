from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import View
from django.http import JsonResponse
from django.utils import timezone

from datetime import datetime

from .models import Project, ProjectVersion, ProjectPatchNote

class ProjectUpdateListView(View):

    def get(self, request, slug, channel):
        # check if the project exists
        project = get_object_or_404(Project, slug__icontains=slug)

        # get the project versions for the project and filter by the channel
        project_versions = get_list_or_404(ProjectVersion.objects.filter(project=project, channel__icontains=channel).order_by('-pk'))

        # even though we're not doing any validation here the get_list_or_404 makes it where we don't really need to validate the index
        latest_version = project_versions[0]

        # create the json object
        json = {}

        json['CurrentUpdate'] = latest_version.version
        json['CurrentUpdateLabel'] = latest_version.version_label.lower()
        json['UpdateChannel'] = channel.lower()

        json['Updates'] = {}

        for p in project_versions:
            tmpDict = {}
            tmpDict[p.version] = { 'ReleaseDate': p.date.strftime('%m/%d/%Y %H:%M:%S %p'), 'CriticalUpdate': p.is_critical_update, 'UpdateLabel': p.version_label, 'DownloadURL': p.download_url }
            
            print(p.date)

            project_patch_notes = ProjectPatchNote.objects.filter(project_version=p)

            tmpAdded = []
            tmpUpdated = []
            tmpFixed = []
            tmpRemoved = []
            tmpDeprecated = []
            tmpSecurity = []
            for pn in project_patch_notes:
                if pn.category == 'Added':
                    tmpAdded.append(pn.description)
                if pn.category == 'Updated':
                    tmpUpdated.append(pn.description)
                if pn.category == 'Fixed':
                    tmpFixed.append(pn.description)
                if pn.category == 'Removed':
                    tmpRemoved.append(pn.description)
                if pn.category == 'Deprecated':
                    tmpDeprecated.append(pn.description)
                if pn.category == 'Security':
                    tmpSecurity.append(pn.description)


            tmpDict[p.version]['PatchNotes'] = {
                'Added': tmpAdded,
                'Updated': tmpUpdated,
                'Fixed': tmpFixed,
                'Removed': tmpRemoved,
                'Deprecated': tmpDeprecated,
                'Security': tmpSecurity,
            }

            json['Updates'].update(tmpDict)

        # json['Updates'] = {
        #     '1.0.0.0': {
        #         'ReleaseDate': 'today',
        #         'CriticalUpdate': False,
        #         'PatchNotes': {
        #             'Added': [],
        #             'Updated': [],
        #             'Fixed': [],
        #             'Removed': [],
        #             'Deprecated': [],
        #             'Security': []
        #         }
        #     }
        # }

        return JsonResponse(json, safe=True)