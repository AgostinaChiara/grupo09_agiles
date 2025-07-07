def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()