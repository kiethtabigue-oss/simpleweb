$path = 'C:\Users\dynas\Downloads\temp_activity.docx'
$item = Get-Item $path
Write-Output "Length: $($item.Length)"
Write-Output "LastWriteTime: $($item.LastWriteTime)"
Write-Output "Attributes: $($item.Attributes)"
$acl = Get-Acl $path
Write-Output "Owner: $($acl.Owner)"
foreach ($access in $acl.Access) {
    Write-Output "$($access.IdentityReference): $($access.FileSystemRights) - Inherited: $($access.IsInherited)"
}