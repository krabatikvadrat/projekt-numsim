"""Make an MP4 play twice as fast at 60 FPS using ffmpeg."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def convert_to_60fps(input_path: Path, output_path: Path) -> None:
	"""Make ``input_path`` play twice as fast at 60 FPS."""
	if shutil.which("ffmpeg") is None:
		raise RuntimeError("ffmpeg is required but was not found on PATH")

	if not input_path.is_file():
		raise FileNotFoundError(f"Input video does not exist: {input_path}")

	output_path.parent.mkdir(parents=True, exist_ok=True)
	command = [
		"ffmpeg",
		"-i",
		str(input_path),
		"-vf",
		"fps=60,setpts=0.1*PTS",
		"-c:v",
		"libx264",
		"-crf",
		"18",
		"-preset",
		"medium",
		"-af",
        "atempo=2.0,atempo=2.0,atempo=2.0,atempo=1.25",
		"-c:a",
		"aac",
		"-y",
		str(output_path),
	]
	subprocess.run(command, check=True)


def main() -> int:
	parser = argparse.ArgumentParser(description="Convert an MP4 video to 60 FPS.")
	parser.add_argument("input", type=Path, help="Path to the source MP4")
	parser.add_argument(
		"output",
		type=Path,
		nargs="?",
		help="Path for the converted MP4 (default: outputs/nbody_60fps.mp4)",
	)
	args = parser.parse_args()

	output_path = args.output or Path(__file__).resolve().parent / "outputs" / "nbody_60fps.mp4"

	try:
		convert_to_60fps(args.input, output_path)
	except (FileNotFoundError, RuntimeError, subprocess.CalledProcessError) as error:
		print(f"Error: {error}", file=sys.stderr)
		return 1

	print(f"Created {output_path}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
