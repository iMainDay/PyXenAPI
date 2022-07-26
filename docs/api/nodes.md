# ``getNodes()`` 
Gets the node tree.

## Parameters
| Parameter      | Type                          | Description                              |
| :---------: | :----------------------------------: | :----------------------------------: |
| `None`       |  |

## Response
| Output      | Type                          | Description                                 |
| :---------: | :----------------------------------: | :----------------------------------: |
| `nodes`       | 	Node[] |  List of all nodes                                                     |

## Example
```py linenums="1"
from PyXenApi import XenForoAPI

xf = XenForoAPI('token', 'domain')

def main():
	data = xf.getNodes()
	return print(json.dumps(data, indent=4, sort_keys=True))
	
if __name__ == '__main__':
	main()
```