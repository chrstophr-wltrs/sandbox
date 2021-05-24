function ConvertTo-Embed {

    param (
        $SrcToEmbed
    )
    
    return '<embed class="embedSvg" src="' + $SrcToEmbed + '" type="image/svg+xml" />'
}

$ImgRegex = '<img src="(.+\.svg)" >'
function ConvertFrom-Svg {

    param (
        $HTMLString
    )

    if ($HTMLString -match $ImgRegex){
        return ($HTMLString -replace $Matches[0], (ConvertTo-Embed -SrcToEmbed $Matches[1]))
    }
    else {
        return $HTMLString
    }
}

function Convert-File {
    param (
        $PathToFile
    )
    
    (ConvertFrom-Svg -HTMLString (Get-Content -path $PathToFile -Raw)) | Set-Content -Path $PathToFile
    
}

Get-ChildItem –Path ".\" -Recurse -Filter *.html | Foreach-Object {

    Convert-File -PathToFile $_.FullName

}