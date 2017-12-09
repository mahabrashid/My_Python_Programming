import dropbox

drpbx = dropbox.Dropbox('CBC0_28g3a4AAAAAAAAFYw7pXTiMzuLD4fMfHYW3L-PokM5o6h34BiniKHP3UHPa')
drpbx.users_get_current_account()

for entry in drpbx.files_list_folder('').entries:
    print(entry.name)