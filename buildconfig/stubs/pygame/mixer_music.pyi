from typing import Optional, Dict

from pygame.typing import FileLike

def load(filename: FileLike, namehint: Optional[str] = "") -> None: ...
def unload() -> None: ...
def play(loops: int = 0, start: float = 0.0, fade_ms: int = 0) -> None: ...
def rewind() -> None: ...
def stop() -> None: ...
def pause() -> None: ...
def unpause() -> None: ...
def fadeout(time: int, /) -> None: ...
def set_volume(volume: float, /) -> None: ...
def get_volume() -> float: ...
def get_busy() -> bool: ...
def set_pos(pos: float, /) -> None: ...
def get_pos() -> int: ...
def queue(filename: FileLike, namehint: str = "", loops: int = 0) -> None: ...
def set_endevent(event_type: int, /) -> None: ...
def get_endevent() -> int: ...
def get_metadata(filename: Optional[FileLike] = None, namehint: str = "") -> Dict[str, str]: ...
