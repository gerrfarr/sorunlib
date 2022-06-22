import sorunlib as run
from sorunlib._internal import check_response


def bias_step():
    """Perform a bias step on all SMuRF Controllers"""
    for smurf in run.CLIENTS['smurf']:
        smurf.take_bias_steps.start()

    for smurf in run.CLIENTS['smurf']:
        resp = smurf.take_bias_steps.wait()
        check_response(resp)


def iv_curve():
    """Perform an iv curve on all SMuRF Controllers"""
    for smurf in run.CLIENTS['smurf']:
        smurf.take_iv.start()

    for smurf in run.CLIENTS['smurf']:
        resp = smurf.take_iv.wait()
        check_response(resp)


def tune_dets(test_mode=False):
    """Perform detector tuning on all SMuRF Controllers.

    Args:
        test_mode (bool): Run tune_dets() task in test_mode, removing emulated
            wait times.

    """
    for smurf in run.CLIENTS['smurf']:
        smurf.tune_dets.start(test_mode=test_mode)

    for smurf in run.CLIENTS['smurf']:
        resp = smurf.tune_dets.wait()
        check_response(resp)


def bias_dets():
    """Bias the detectors on all SMuRF Controllers"""
    for smurf in run.CLIENTS['smurf']:
        smurf.bias_dets.start()

    for smurf in run.CLIENTS['smurf']:
        resp = smurf.bias_dets.wait()
        check_response(resp)


def stream(state):
    """Stream data on all SMuRF Controllers.

    Args:
        state (str): Streaming state, either 'on' or 'off'.

    """
    if state.lower() == 'on':
        for smurf in run.CLIENTS['smurf']:
            smurf.stream.start()

        for smurf in run.CLIENTS['smurf']:
            print(smurf.stream.status())
    else:
        for smurf in run.CLIENTS['smurf']:
            smurf.stream.stop()
            resp = smurf.stream.wait()
            check_response(resp)
            print(resp)
