github_repo_latest = "https://api.github.com/repos/kartFr/Auto-Animation-Reuploader/releases/latest"
asset_delivery = "https://assetdelivery.roblox.com/v1/asset/?id="
asset_info = "https://develop.roblox.com/v1/assets?assetIds="
authenticated = "https://users.roblox.com/v1/users/authenticated"

def getPublishUrl(assetTypeName, name, creatorId, isGroup):
    return (
        "https://www.roblox.com/ide/publish/uploadnewanimation?"
        f"assetTypeName={ assetTypeName }"
        f"&name={ name }"
        "&description=Forgium Studios Animation"
        "&AllID=1"
        "&ispublic=False"
        "&allowComments=True"
        "&isGamesAsset=False"
        f"{ '&groupId=' + str(creatorId) if isGroup else '' }"
    )
