from selenium.webdriver.common.by import By


class CheckBoxLocators:
    expand_all = (By.XPATH, '//*[@id="tree-node"]/div/button[1]')
    select_tree_node_home = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/label')
    check_text_tree_node_home = (By.XPATH, '//*[@id="result"]/span[2]')
    select_tree_node_desktop = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/span/label')
    check_text_tree_node_desktop = (By.XPATH, '//*[@id="result"]/span[2]')