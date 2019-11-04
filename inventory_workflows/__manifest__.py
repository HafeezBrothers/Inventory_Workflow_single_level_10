{
    'name':   'Inventory Workflows',
    'author': 'Hafeez Brothers',

    'depends': [
                'base',
                
                'stock'
                
                ],
    
    'data': [
      
        'Views/stock_picking_workflow.xml',
        'security/hr_user_rights_inventory.xml'
    ],
    
    'application': True,
    'price':25.00,
    'currency':'EUR', 
}
