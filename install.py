import launch

if not launch.is_installed("pillow"):
    launch.run_pip("install pillow")