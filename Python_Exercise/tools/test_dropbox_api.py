import dropbox

drpbx = dropbox.Dropbox('')
drpbx.users_get_current_account()

for entry in drpbx.files_list_folder('').entries:
    print(entry.name)