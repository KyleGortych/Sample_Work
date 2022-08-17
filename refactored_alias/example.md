# Refactored brew List Packages No Dependancies

## A Modest Speedup

<img width="1000" alt="refactored aliase" src="https://raw.githubusercontent.com/KyleGortych/sample_work/main/refactored_alias/Refactored%20brew%20list.png">

## fish Shell Aliases

<details>
<summary>example</summary>

``` fish
function brew-ls
  sed -n '/Packages/,/pip/{/pip/!p;}' ~/.config/fish/Shell_Support/alias_script_support/build_sys.txt
end

function brew-seach
  echo -e '\e[4mPackages no Depens\e[0m' ; brew leaves | column ; echo '' ; echo -e '\e[4mCasks\e[0m' ; brew list --cask ; echo '' ; echo -e '\e[4mTaps\e[0m' ; brew tap-info --installed
end
```
</details>

## Semi-Auto
<details>
<summary>Past from fish alias stdout. Lastly use command below while in visual mode in vim.</summary>
  
``` vim
:'<,'>!column -t
```

</details>

## result
<details>
<summary>example</summary>
<pre>
Packages no Depens   Casks
-------------------  ------
pkg1 pkg4 pkg7       cask1 cask4 cask7
pkg2 pkg5 pkg8       cask2 cask5 cask8
pkg3 pkg6 pkg9       cask3 cask6 cask9
</pre>
<pre>
Taps/3d Party
--------------
name: num casks
/usr/local/Homebrew/Library/Taps/ (num files, num KB)
From: https://github.com/pkg-name
</pre>
</details>

## future work
  <details>
  <summary>benchmark aliases via fish shell</summary>
  
  ``` fish
  function command_name
    time $argv[1]& time $argv[1]& time $argv[2]& time $argv&
    or time $argv[1]& seq n && time $argv[2]& seq n
    some_filter | print difference
  end
  ```
  </details>
