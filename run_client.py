import argparse
from whisper_live.client import TranscriptionClient

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port',
                        type=int,
                        default=9090,
                        help="Websocket port to run the server on.")
    parser.add_argument('--language',
                        type=str,
                        default="lt",
                        help='Language')
    parser.add_argument('--model',
                        type=str,
                        default="large-v2",
                        help='model type')
    parser.add_argument('--use_vad',
                        type=bool,
                        default=False,
                        help="Use vad?")
    parser.add_argument('--hls_url',
                        type=str,
                        default="https://stream-live.lrt.lt/lituanica/stream04/streamPlaylist.m3u8",
                        help="hls stream")
    
    args = parser.parse_args()

    client = TranscriptionClient("localhost",
                                 args.port,
                                 lang=args.language,
                                 translate=False,
                                 model=args.model,
                                 use_vad=args.use_vad)

    client(hls_url=args.hls_url)