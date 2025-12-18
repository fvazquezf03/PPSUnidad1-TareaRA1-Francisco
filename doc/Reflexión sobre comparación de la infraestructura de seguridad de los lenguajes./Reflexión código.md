# Reflexión sobre medidas de seguridad en lenguajes de programación

## Introducción

En este texto reflexiono sobre las medidas de seguridad que incorporan algunos de los principales lenguajes de programación y cómo estas medidas influyen en la seguridad de las aplicaciones en producción. La reflexión sirve como entrada para el apartado 5 de la Tarea Obligatoria de la Unidad 1.


## Conclusión personal

En mi opinión, no existe un único "lenguaje seguro" por sí mismo: la seguridad es una combinación de diseño del lenguaje, ecosistema, herramientas y prácticas operativas. Si el objetivo es minimizar errores de memoria y concurrencia, Rust ofrece una ventaja clara por su modelo de propiedad y comprobaciones en compilación. Si la prioridad es productividad con protecciones por defecto, un lenguaje gestionado como Java o C# es adecuado.

Para aplicaciones que se van a analizar en sandboxing (ej. ejecución de código potencialmente inseguro o análisis de malware), mi recomendación práctica es:

- Usar entornos aislados (contenedores, Firejail, VMs) para cualquier código no verificado.
- Emplear análisis estático y dinámico (fuzzing, sanitizers) cuando sea posible.
- Mantener control estricto de dependencias y políticas de permisos.



