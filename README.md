# nngtools

## Usage

1. Place your `nngsave.json` to the directory in which you want to extract the level files.
1. Place `nngmap.json` on the same directory.
1. Run `nngsave2files.py nngsave.json`.
   This should create a bunch of wold dirs / level files.

## How to save/load your game

The following is taken from [this message][leanprover-zulip-saveload] by [mpedramfar][mpedramfar].
I have altered the savegame javascript code to:
(i) prettyprint the json file instead of dumping it as a single line, and also the filename chosen;
(ii) use the name `nngsave.json` for the created file.

Create the bookmarks:

* `nng-save`, using the following URL:
```
javascript:(function save(data, filename) { if(!window.location.href.endsWith("natural_number_game/")){ alert("To load saved game, go to the main page first!"); return;  }; var file = new Blob([JSON.stringify(JSON.parse(data), null, 2)]); var a = document.createElement("a"), url = URL.createObjectURL(file); a.href = url; a.download = filename; document.body.appendChild(a); a.click(); setTimeout(function() { document.body.removeChild(a); window.URL.revokeObjectURL(url);  }, 0);  })(window.localStorage.getItem("Natural number game-1-savedGameData"), "nngsave.json");
```

* `nng-load`, with the following URL:
```
javascript:(function(){ return new Promise((resolve) => { if(!window.location.href.endsWith("natural_number_game/")){ alert("To load saved game, go to the main page first!"); resolve("");  }else{ const uploader = document.createElement('input'); uploader.type = 'file'; uploader.style.position = 'relative'; uploader.addEventListener('change', () => { const files = uploader.files; if (files.length) { const reader = new FileReader(); reader.addEventListener('load', () => { uploader.parentNode.removeChild(uploader); resolve(reader.result);  }); reader.readAsText(files[0]);  };  }); document.body.appendChild(uploader); document.getElementById("root").style.display = 'none';  };  });  })().then(text => { console.log(text); if(text){ window.localStorage.setItem("Natural number game-1-savedGameData", text); window.location.reload();  };  });
```

## Notes

The file `nngmap.json` contains a map from level statements to world and level numbers.
This file is created by running `mknngmap.py` on a complete nng savegame, placed on the `src/game` directory of [natural_number_game][nng-github].
Normally you will not need to run this; you can just use the `nngmap.json` provided here.


[nng-github]: https://github.com/ImperialCollegeLondon/natural_number_game
[mpedramfar]: https://github.com/mpedramfar
[leanprover-zulip-saveload]: https://leanprover.zulipchat.com/#narrow/stream/187764-Lean-for.20teaching/topic/submit.20or.20share.20nng.20solutions/near/263776473
