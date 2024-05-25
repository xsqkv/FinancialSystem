import {Card} from "primereact/card";
import {Divider} from "primereact/divider";
import {fetchCategoryProductCountSaleQuery} from "@/hooks/api/analytics/category/fetchCategoryProductCountSale";


const AnalyticCategoryProductCountSale = function (props) {

  const {data, isPending, isError} = fetchCategoryProductCountSaleQuery(props.category_id)

  const header =
    <div className='pt-3'>
      <div className='flex flex-row px-3 justify-content-between'>
        <div>
          <div className='text-2xl'>Количество товаров</div>
          <div className='text-xs'>Кол-во проданных по данной категории</div>
        </div>
      </div>
      <Divider/>
    </div>


  if (isError) {
    return <div>Error</div>
  }

  return (
    <Card header={header}>
      <div>
        <div className='text-4xl font-bold text-blue-600'>{isPending ? 'Загрузка' : data.category_product_count_sale.toLocaleString('ru-RU')}</div>
        <div className='text-1xl'>За весь период</div>
      </div>
    </Card>
  )
}

export default AnalyticCategoryProductCountSale
